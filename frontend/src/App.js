import React from "react";
import { Switch, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import Landing from "./Containers/Landing";
import Home from "./Containers/Home";

import Nav from "./Components/Nav";
import ProtectedRoute from "./Components/ProtectedRoute";

import "react-toastify/dist/ReactToastify.css";

const App = () => {
	return (
		<>
			<ToastContainer />
			<Nav />
			<Switch>
				<Route exact path="/">
					<Landing />
				</Route>
				<Route path={["/dashboard", "/forms", "/create", "/data"]}>
					<ProtectedRoute>
						<Home />
					</ProtectedRoute>
				</Route>
			</Switch>
		</>
	);
};

export default App;
