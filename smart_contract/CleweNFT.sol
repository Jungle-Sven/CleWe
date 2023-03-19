// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.4.22 <0.9.0;
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CLWNFT is ERC721URIStorage{
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    event NewNFTMinted(address sender, uint256 tokenId, string tokenURI);

    constructor() ERC721 ("Clewe NFT", "CLW-NFT") {}

    function mintItem(string memory tokenURI) public{
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        emit NewNFTMinted(msg.sender, newItemId, tokenURI);
    }

    function updateMetadata(uint256 tokenId, string memory newURI) public {
    require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
    require(_isApprovedOrOwner(msg.sender, tokenId), "ERC721Metadata: caller is not owner nor approved");
    
    _setTokenURI(tokenId, newURI);
    }

    // Do nothing or revert to prevent following functions from being used
    function transferFrom(address from, address to, uint256 tokenId) public override {
    revert("This function is disabled.");
    }

    function approve(address to, uint256 tokenId) public override {
        revert("This function is disabled.");
    }

    function safeTransferFrom(address from, address to, uint256 tokenId, bytes memory _data) public override {
        revert("This function is disabled.");
    }

    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        revert("This function is disabled.");
    }

    function setApprovalForAll(address operator, bool approved) public override {
        revert("This function is disabled.");
    }

    function getApproved(uint256 tokenId) public view override returns (address) {
        revert("This function is disabled.");
    }

    function isApprovedForAll(address owner, address operator) public view override returns (bool) {
        revert("This function is disabled.");
    }
}