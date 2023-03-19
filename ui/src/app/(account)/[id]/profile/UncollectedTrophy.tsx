"use client";

import Image from "next/image";
import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { UserDTO } from "../model";
import { mintNFTTrophy } from "./mintNFTTrophy";
import styles from "./page.module.css";

type Props = {
  user: UserDTO;
  id: number;
  image: string;
  description: string;
};

export default function UncollectedTrophy({
  user,
  id,
  image,
  description,
}: Props) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [isFetching, setIsFetching] = useState(false);

  // Create inline loading UI
  const isMutating = isFetching || isPending;

  async function mint() {
    setIsFetching(true);
    const txnHash = await mintNFTTrophy({
      imgURL: image,
      nickname: user.nickname,
      level: user.level,
      skills: user.skills,
    });
    console.log("Transcation completed!", txnHash);

    await fetch(`${process.env.NEXT_PUBLIC_APP_URL}/api/trophies/${id}`, {
      method: "PUT",
      body: JSON.stringify({
        tx_hash: txnHash,
      }),
    });

    setIsFetching(false);

    startTransition(() => {
      router.refresh();
    });
  }

  return (
    <div className={styles.achievementBox}>
      <div className={styles.achievementBoxInfoWrap}>
        <Image
          className={styles.achievementBoxImage}
          src={image}
          alt="quest-completedq-l"
          width={82}
          height={90}
        />

        <div className={styles.achievementBoxInfo}>
          <p className={styles.achievementBoxTitle}>Reward is available!</p>
          <p className={styles.achievementBoxText}>{description}</p>
        </div>
      </div>

      <button
        className={styles.achievementBoxButton}
        type="button"
        disabled={isMutating}
        onClick={mint}
      >
        Take the NFT
      </button>
    </div>
  );
}
