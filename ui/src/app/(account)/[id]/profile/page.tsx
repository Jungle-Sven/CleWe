import Image from "next/image";
import styles from "./page.module.css";
import layout from "../../layout.module.css";
import avatar from "../img/avatar.jpg";
import { ProgressLine } from "../../ProgressLine";
import classNames from "classnames";
import UncollectedTrophy from "./UncollectedTrophy";
import CollectedTrophy from "./CollectedTrophy";
import { UserDTO } from "../model";

async function getUser(id: string): Promise<UserDTO> {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/api/users/${id}`,
    { cache: "no-store" }
  );
  const resJ = await res.json();
  return resJ;
}

type Params = {
  id: string;
};

export default async function Profile({ params }: { params: Params }) {
  const user = await getUser(params.id);
  const currentLevelProgress = Math.floor(
    ((user.level_total_exp - user.exp_to_next_level) / user.level_total_exp) *
      100
  );

  return (
    <div className={layout.content}>
      <div className={layout.grid}>
        <div
          className={classNames(
            layout.grid,
            styles.achievements,
            styles.grid22
          )}
        >
          {user.trophies
            .filter((trophy) => !trophy.tx_hash)
            .map((trophy) => (
              <UncollectedTrophy
                key={trophy.id}
                id={trophy.id}
                image={`${process.env.NEXT_PUBLIC_APP_URL}/${trophy.img_url}`}
                description={trophy.description}
                user={user}
              />
            ))}
        </div>

        <div className={classNames(layout.grid, layout.grid39)}>
          <div
            className={classNames(
              layout.contentWidget,
              styles.profilePersonality
            )}
          >
            <div className={styles.profilePersonalityCover}>
              <p className={styles.profilePersonalityCoverTitle}>
                Welcome back!
              </p>
            </div>
            <div className={styles.profilePersonalitySummary}>
              <div className={styles.profilePersonalityAvatar}>
                <Image
                  className={styles.profilePersonalityAvatarImage}
                  src={avatar}
                  alt="Profile avatar"
                  height={100}
                  width={100}
                />
              </div>
              <div className={styles.profilePersonalitySummaryTitle}>
                <p>{user.nickname}</p>
              </div>
            </div>
          </div>

          <div
            className={classNames(
              layout.grid,
              styles.profileStats,
              styles.noMargin
            )}
          >
            <div
              className={classNames(
                layout.contentWidget,
                styles.levelProgressBox
              )}
            >
              <div className={styles.levelProgressBadge}>
                <p className={styles.levelProgressBadgeText}>{user.level}</p>
              </div>
              <div className={styles.levelProgressStats}>
                <div className={styles.progressBarWrap}>
                  <p className={styles.progressBarInfo}>
                    +{user.exp_to_next_level} EXP
                    <span className={styles.light}>
                      to reach the next level
                    </span>
                  </p>
                </div>
                <div className={styles.expToNextLevel}>
                  <ProgressLine progress={currentLevelProgress} />
                </div>
              </div>
            </div>

            <div className={classNames(layout.grid, layout.grid333)}>
              {user.skills.map((skill) => (
                <div
                  key={skill.id}
                  className={classNames(
                    layout.contentWidget,
                    styles.reputationStats,
                    styles[`stats${Math.ceil(Math.random() * 3)}`]
                  )}
                >
                  <p className={styles.reputationStatsNumber}>
                    {skill.experience}
                  </p>
                  <p className={styles.reputationStatsTopic}>{skill.topic}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
        {/* Collected Trophies */}
        <div className={classNames(layout.grid, layout.grid3333)}>
          {user.trophies
            .filter((trophy) => trophy.tx_hash)
            .map((trophy) => (
              <CollectedTrophy
                key={trophy.id}
                imgUrl={`${process.env.NEXT_PUBLIC_APP_URL}/${trophy.img_url}`}
                description={trophy.description}
                txnHash={trophy.tx_hash as string}
              />
            ))}
        </div>
      </div>
    </div>
  );
}
