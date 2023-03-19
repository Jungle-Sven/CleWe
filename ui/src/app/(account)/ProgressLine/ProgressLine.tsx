import styles from "./styles.module.css";

type Props = {
  progress: number;
  height?: number;
};

export function ProgressLine({ progress, height }: Props) {
  return (
    <div className={styles.visualFull} style={{ height: `${height || 6}px` }}>
      <div
        className={styles.visualProgressPart}
        style={{
          width: `${progress}%`,
        }}
      ></div>
    </div>
  );
}
