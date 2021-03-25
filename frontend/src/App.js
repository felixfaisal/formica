import React from "react";
import { Switch, Route } from "react-router-dom";

import Landing from "./Containers/Landing";

import Nav from "./Components/Nav";

const App = () => {
	return (
		<>
			<Nav />
			<Switch>
				<Route exact path="/">
					<Landing />
				</Route>
			</Switch>
		</>
	);
};

export default App;
