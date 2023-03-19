import classNames from "classnames";
import styles from "./page.module.css";
import layout from "../../layout.module.css";
import openedQuest from "./img/openq-b.png";
import completedQuest from "./img/completedq-b.png";
import Image from "next/image";
import Link from "next/link";
import { QuestDTO, UserDTO } from "../model";
import { ProgressLine } from "../../ProgressLine";

export const revalidate = 0;

type Quest = QuestDTO & {
  completed: boolean;
};

async function getQuests(userId: string): Promise<Quest[]> {
  const questsDTO = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/api/quests`,
    {
      cache: "no-store",
    }
  );
  const userDTO = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/api/users/${userId}`,
    { cache: "no-store" }
  );
  const userObj = (await userDTO.json()) as UserDTO;
  const resObj = (await questsDTO.json()) as QuestDTO[];
  const questsWithCompletionMark = resObj.map(
    (quest) =>
      ({
        ...quest,
        completed: userObj.completed_quests.some(
          (complQ) => complQ.id === quest.id
        ),
      } as Quest)
  );
  return questsWithCompletionMark;
}

type Params = {
  id: string;
};

const MAX_DIFFICULTY = 5;

export default async function Page({ params }: { params: Params }) {
  const featuredQuests = await getQuests(params.id);

  return (
    <div className={layout.content}>
      <div className={layout.grid}>
        <div className={styles.titleBanner}>
          <p className={styles.titleBannerTitle}>Quests</p>
          <p className={styles.titleBannerDescription}>
            Impove your knowledge, gain reputation, play, earn rewards
          </p>
        </div>
        <div className={styles.questsHeader}>
          <p className={styles.questsHeaderTitle}>Featured Quests</p>
        </div>
        <div className={classNames(layout.grid, layout.grid3333)}>
          {featuredQuests.map((quest) => (
            <div
              key={quest.id}
              className={classNames(layout.contentWidget, styles.questItem)}
            >
              <div className={styles.questItem}>
                {quest.completed ? null : (
                  <p className={styles.questExpSticker}>
                    + {quest.exp_reward} EXP
                  </p>
                )}
                <div
                  className={classNames(
                    styles.questItemCover,
                    styles[`cover${Math.ceil(Math.random() * 4)}`]
                  )}
                />
                <div className={styles.questItemInfo}>
                  <div className={styles.questItemBadge}>
                    <Image
                      src={quest.completed ? completedQuest : openedQuest}
                      alt="Quest status"
                    />
                  </div>
                  <p className={styles.questItemTitle}>{quest.topic}</p>
                  <p className={styles.questItemDescription}>
                    {quest.description}
                  </p>
                  <div className={styles.questDifficultyWrapper}>
                    <ProgressLine
                      progress={Math.floor(
                        (quest.difficulty / MAX_DIFFICULTY) * 100
                      )}
                      height={4}
                    />
                    <p className={styles.questDifficultyTitle}>Difficulty</p>
                  </div>
                  <div className={styles.questActions}>
                    {quest.completed ? (
                      <p className={styles.questItemCompletedStatus}>
                        Completed!
                      </p>
                    ) : (
                      <Link
                        className={classNames("button", styles.questLink)}
                        href={`${params.id}/quests/${quest.slug}`}
                      >
                        Start
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
