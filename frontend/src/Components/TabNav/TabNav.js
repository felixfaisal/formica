import React from "react";
import { useLocation, Link } from "react-router-dom";

import styles from "./TabNav.module.css";

import tabs from "../../Assets/Data/tabs";

const TabNav = () => {
	const location = useLocation();

	const displayTabs = tabs.map((tab) => (
		<Link to={tab.path} className={`${styles.tab} ${location.pathname === tab.path ? styles.active_tab : null}`}>
			{tab.title}
		</Link>
	));

	return <div className={styles.container}>{displayTabs}</div>;
};

export default TabNav;
