import styles from "./Module.module.css";

const Module = () => {
  return (
    <main>
      <h2>Module 페이지</h2>
      <section className={styles.container}>
        <h2>컨테이너아이템</h2>
        <h2>컨테이너아이템</h2>
        <h2>컨테이너아이템</h2>
      </section>
    </main>
  );
};

export default Module;
