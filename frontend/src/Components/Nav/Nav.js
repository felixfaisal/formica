import React from "react";

import Button from "../Button";

import styles from "./Nav.module.css";

import { ReactComponent as DiscordLogo } from "../../Assets/Images/discord.svg";

const Nav = () => {
	return (
		<nav className={styles.nav}>
			<span className={styles.brand}>
				<DiscordLogo className={styles.logo} />
				<h3>Formica</h3>
			</span>
			<Button title="Login" />
		</nav>
	);
};

export default Nav;
