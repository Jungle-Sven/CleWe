import classNames from "classnames";
import styles from "./page.module.css";
import layout from "../layout.module.css";
import openedQuest from "./img/openq-b.png";
import completedQuest from "./img/completedq-b.png";
import Image from "next/image";
import Link from "next/link";

export default function Page() {
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
          <div className={classNames(layout.contentWidget, styles.questItem)}>
            <div className={styles.questItem}>
              <div
                className={classNames(styles.questItemCover, styles.cover1)}
              />
              <div className={styles.questItemInfo}>
                <div className={styles.questItemBadge}>
                  <Image src={openedQuest} alt="Quest status" />
                </div>
                <p className={styles.questItemTitle}>DEX introduction</p>
                <p className={styles.questItemDescription}>
                  SOme desc goes here
                </p>
                <div className={styles.questActions}>
                  <Link
                    className={classNames("button", styles.questLink)}
                    href="#"
                  >
                    Start
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <div className={classNames(layout.contentWidget, styles.questItem)}>
            <div className={styles.questItem}>
              <div
                className={classNames(styles.questItemCover, styles.cover2)}
              />
              <div className={styles.questItemInfo}>
                <div className={styles.questItemBadge}>
                  <Image src={openedQuest} alt="Quest status" />
                </div>
                <p className={styles.questItemTitle}>L1 systems</p>
                <p className={styles.questItemDescription}>
                  SOme desc goes here
                </p>
                <div className={styles.questActions}>
                  <Link
                    className={classNames("button", styles.questLink)}
                    href="#"
                  >
                    Start
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <div className={classNames(layout.contentWidget, styles.questItem)}>
            <div className={styles.questItem}>
              <div
                className={classNames(styles.questItemCover, styles.cover3)}
              />
              <div className={styles.questItemInfo}>
                <div className={styles.questItemBadge}>
                  <Image src={openedQuest} alt="Quest status" />
                </div>
                <p className={styles.questItemTitle}>Crypto wallets</p>
                <p className={styles.questItemDescription}>
                  SOme desc goes here
                </p>
                <div className={styles.questActions}>
                  <Link
                    className={classNames("button", styles.questLink)}
                    href="#"
                  >
                    Start
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <div className={classNames(layout.contentWidget, styles.questItem)}>
            <div className={styles.questItem}>
              <div
                className={classNames(styles.questItemCover, styles.cover4)}
              />
              <div className={styles.questItemInfo}>
                <div className={styles.questItemBadge}>
                  <Image src={openedQuest} alt="Quest status" />
                </div>
                <p className={styles.questItemTitle}>Trading</p>
                <p className={styles.questItemDescription}>
                  SOme desc goes here
                </p>
                <div className={styles.questActions}>
                  <Link
                    className={classNames("button", styles.questLink)}
                    href="#"
                  >
                    Start
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
