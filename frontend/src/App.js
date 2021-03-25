import React from "react";
import { Switch, Route } from "react-router-dom";

import Landing from "./Containers/Landing";
import Dashboard from "./Containers/Dashboard";
import Home from "./Containers/Home";

import Nav from "./Components/Nav";

const App = () => {
	return (
		<>
			<Nav />
			<Switch>
				<Route exact path="/">
					<Landing />
				</Route>
				<Route path={["/dashboard", "/forms", "/create", "/data"]}>
					<Home />
				</Route>
			</Switch>
		</>
	);
};

export default App;
