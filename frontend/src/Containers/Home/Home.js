import React from "react";
import { Route, Switch } from "react-router";

import Dashboard from "../Dashboard";

import TabNav from "../../Components/TabNav/TabNav";

import styles from "./Home.module.css";

const Home = () => {
	return (
		<div className={styles.container}>
			<div>
				<TabNav />
			</div>
			<div>
				<Switch>
					<Route exact path="/dashboard">
						<Dashboard />
					</Route>
				</Switch>
			</div>
		</div>
	);
};

export default Home;
