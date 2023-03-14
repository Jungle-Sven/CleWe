import Image from "next/image";
import { Inter } from "next/font/google";
import styles from "./page.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <main className={styles.main}>
      <p>
        This will be a landing page, from where user can be redirected to login,
        or to personal account
      </p>
    </main>
  );
}
