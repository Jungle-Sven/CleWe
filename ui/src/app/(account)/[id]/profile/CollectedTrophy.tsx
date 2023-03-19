import classNames from "classnames";
import styles from "./page.module.css";
import layout from "../../layout.module.css";
import Image from "next/image";
import Link from "next/link";

type Props = {
  imgUrl: string;
  description: string;
  txnHash: string;
};

export default function CollectedTrophy({
  imgUrl,
  description,
  txnHash,
}: Props) {
  return (
    <Link href={`${process.env.BLOCKHAIN_URL}/${txnHash}`} target="_blank">
      <div
        className={classNames(layout.contentWidget, styles.uncollectedTrophy)}
      >
        <div>
          <Image src={imgUrl} alt="Your trophy" width={82} height={82} />
        </div>
        <p className={styles.uncollectedTrophyDescription}>{description}</p>
        <div className={styles.uncollectedTrophyStatusWrapper}>
          <p className={styles.uncollectedTrophyStatusText}>Unlocked!</p>
        </div>
      </div>
    </Link>
  );
}
