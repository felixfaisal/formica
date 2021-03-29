import React from "react";

import Button from "../../Components/Button";

import styles from "./Landing.module.css";

import { ReactComponent as Hero } from "../../Assets/Images/hero.svg";

const Landing = () => {
	return (
		<div className={styles.container}>
			<div className={styles.info}>
				<h1>Formica</h1>
				<h2>In-Discord Forms Solution</h2>
				<p>
					Formica allows you to create forms and collect responses from users without having them ever leave
					their favourite app, Discord! Formica is fully transparent and allows users to see where their data
					is being shared and allows them to delete the data if they wish to.
				</p>
				<Button title="Let's Go!" />
			</div>
			<div>
				<Hero className={styles.hero} />
			</div>
		</div>
	);
};

export default Landing;
