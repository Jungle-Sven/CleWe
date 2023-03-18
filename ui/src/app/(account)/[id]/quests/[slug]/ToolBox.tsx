"use client";

import { useRouter } from "next/navigation";
import styles from "./page.module.css";

async function completeQuest({
  slug,
  userId,
}: {
  slug: string;
  userId: string;
}) {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_APP_URL}/api/quests/${slug}/complete`,
    {
      method: "PATCH",
      body: JSON.stringify({
        user_id: userId,
      }),
    }
  );
  const resJ = await res.json();
  return resJ;
}

type Props = {
  slug: string;
  userId: string;
};

export default function ToolBox({ slug, userId }: Props) {
  const router = useRouter();
  return (
    <div className={styles.toolbox}>
      <button
        className={styles.completeButton}
        type="button"
        onClick={() =>
          completeQuest({ slug, userId }).then(() =>
            router.push(`/${userId}/quests`)
          )
        }
      >
        Complete
      </button>
    </div>
  );
}
