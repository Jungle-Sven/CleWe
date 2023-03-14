import styles from "./styles.module.css";

type Props = {
  progress: number;
};

export function ProgressLine({ progress }: Props) {
  return (
    <div className={styles.visualFull}>
      <div
        className={styles.visualProgressPart}
        style={{
          width: `${progress}%`,
        }}
      ></div>
    </div>
  );
}
