import React from "react";

import TabNav from "../../Components/TabNav/TabNav";

import styles from "./Home.module.css";

const Home = () => {
	return (
		<div className={styles.container}>
			<div>
				<TabNav />
			</div>
			<div></div>
		</div>
	);
};

export default Home;
