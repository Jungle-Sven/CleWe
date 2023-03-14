import Link from "next/link";
import classNames from "classnames";
import styles from "./layout.module.css";

export const metadata = {
  title: "Account",
  description: "Accout of the clewer",
};

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <header className={styles.header}>
        {/* HEADER ACTIONS */}
        <div className={styles.headerActions}>
          {/* HEADER BRAND */}
          <div className={styles.headerBrand}>
            {/* HEADER BRAND TEXT */}
            <h1 className={styles.headerBrandText}>CleWe</h1>
            {/* /HEADER BRAND TEXT */}
          </div>
          {/* /HEADER BRAND */}
        </div>
        {/* /HEADER ACTIONS */}

        <nav className={styles.navigation}>
          <ul className={styles.mainMenu}>
            <li>
              <Link
                className={styles.mainMenuLink}
                href="/id_placeholder/profile"
              >
                Profile
              </Link>
            </li>
            <li>
              <Link className={styles.mainMenuLink} href="/quests">
                Quests
              </Link>
            </li>
          </ul>
        </nav>
      </header>
      {/* /HEADER */}
      <main>{children}</main>
    </>
  );
}
