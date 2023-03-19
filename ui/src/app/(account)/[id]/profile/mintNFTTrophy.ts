import { NFTStorage, File } from "nft.storage";
import detectEthereumProvider from "@metamask/detect-provider";
import { createAlchemyWeb3 } from "@alch/alchemy-web3";
import contractABI from "./contract-abi.json";
import { blob } from "stream/consumers";

const web3 = createAlchemyWeb3(
  process.env.NEXT_PUBLIC_ALCHEMY_API_KEY as string
);

type Metadata = {
  imgURL: string;
  nickname: string;
  level: number;
  skills: Object[];
};

type txnHash = string;

export async function mintNFTTrophy(metadata: Metadata): Promise<txnHash> {
  try {
    const walletAddress = await connectWallet();
    const { url: ipsfURL } = await uploadNFTMetadata(metadata);
    console.log("METADATA URL", ipsfURL);
    const contract = await new web3.eth.Contract(
      contractABI as any,
      process.env.NEXT_PUBLIC_SMART_CONTRACT_ADDRESS
    );
    // Send transaction to the Ethereum network
    const txnHash = await window.ethereum.request({
      method: "eth_sendTransaction",
      params: [
        {
          from: walletAddress,
          to: process.env.NEXT_PUBLIC_SMART_CONTRACT_ADDRESS,
          data: contract.methods.mintItem(ipsfURL).encodeABI(),
        },
      ],
    });
    return txnHash;
  } catch (error: any) {
    throw new Error(error);
  }
}

async function connectWallet() {
  const provider = await detectEthereumProvider();

  if (!provider) {
    throw new Error("Please install MetaMask!");
  }

  if (provider !== window.ethereum) {
    throw new Error("Seems like you have multiple wallets installed");
  }

  try {
    const connectedAccounts = await window.ethereum.request({
      method: "eth_accounts",
    });
    if (connectedAccounts.length === 0) {
      console.warn("Metamask account is not connected... trying to connect");
      const requestedAccounts = await window.ethereum.request({
        method: "eth_requestAccounts",
      });
      if (requestedAccounts.length === 0) {
        console.warn("Please connect to MetaMask.");
        return undefined;
      }
      return requestedAccounts[0] as string;
    } else {
      // bypass request flow
      return connectedAccounts[0] as string;
    }
  } catch (error: any) {
    throw new Error(error);
  }
}

async function uploadNFTMetadata({
  imgURL,
  nickname,
  level,
  skills,
}: Metadata) {
  const image = await loadImageFromUrl(imgURL);
  const nftStorage = new NFTStorage({
    token: process.env.NEXT_PUBLIC_NFT_STORAGE_KEY as string,
  });
  return nftStorage.store({
    image,
    name: `Clewe Skills`,
    description: "Test instance of NFT Trophy minted for CleWe user",
    properties: {
      nickname,
      level,
      skills,
    },
  });
}

async function loadImageFromUrl(url: string) {
  const response = await fetch(url);
  const imgContent = await response.blob();
  return new File([imgContent], imgContent.name, { type: imgContent.type });
}
