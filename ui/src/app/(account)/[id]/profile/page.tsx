import Image from "next/image";
import styles from "./page.module.css";
import layout from "../../layout.module.css";
import completedq from "../img/completedq-l.png";
import avatar from "../img/avatar.jpg";
import { ProgressLine } from "../../ProgressLine";
import classNames from "classnames";

export default function Profile() {
  return (
    <div className={layout.content}>
      <div className={layout.grid}>
        <div className={classNames(layout.grid, styles.achievements)}>
          <div className={styles.achievementBox}>
            <div className={styles.achievementBoxInfoWrap}>
              <Image
                className={styles.achievementBoxImage}
                src={completedq}
                alt="quest-completedq-l"
              />

              <div className={styles.achievementBoxInfo}>
                <p className={styles.achievementBoxTitle}>Skill improved!</p>
              </div>
            </div>

            <button className={styles.achievementBoxButton} type="button">
              Take the NFT prize
            </button>
          </div>
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
                <p>Nickname here</p>
              </div>
            </div>
          </div>

          <div className={classNames(layout.grid, styles.profileStats)}>
            <div
              className={classNames(
                layout.contentWidget,
                styles.levelProgressBox
              )}
            >
              <div className={styles.levelProgressBadge}>
                <p className={styles.levelProgressBadgeText}>2</p>
              </div>
              <div className={styles.levelProgressStats}>
                <div className={styles.progressBarWrap}>
                  <p className={styles.progressBarInfo}>
                    +38 EXP
                    <span className={styles.light}>
                      to reach the next level
                    </span>
                  </p>
                </div>
                <div className={styles.expToNextLevel}>
                  <ProgressLine progress={40} />
                </div>
              </div>
            </div>

            <div className={classNames(layout.grid, layout.grid333)}>
              <div
                className={classNames(
                  layout.contentWidget,
                  styles.reputationStats,
                  styles.stats1
                )}
              >
                <p className={styles.reputationStatsNumber}>2.6</p>
                <p className={styles.reputationStatsTopic}>DEX reputation</p>
              </div>
              <div
                className={classNames(
                  layout.contentWidget,
                  styles.reputationStats,
                  styles.stats2
                )}
              >
                <p className={styles.reputationStatsNumber}>0.1</p>
                <p className={styles.reputationStatsTopic}>
                  CryptoWallets reputation
                </p>
              </div>
              <div
                className={classNames(
                  layout.contentWidget,
                  styles.reputationStats,
                  styles.stats3
                )}
              >
                <p className={styles.reputationStatsNumber}>1.8</p>
                <p className={styles.reputationStatsTopic}>
                  L1 systems reputation
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
