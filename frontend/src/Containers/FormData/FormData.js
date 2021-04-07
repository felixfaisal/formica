import React from "react";
import { Switch, Route, Link, useParams } from "react-router-dom";

import FormResponses from "../FormResponses";
import FormStatistics from "../FormStatistics";

import styles from "./FormData.module.css";

const FormData = () => {
	const { id } = useParams();

	return (
		<>
			<h3 className={styles.title}>Form {id} :- </h3>
			{/* <div className={styles.tabs}>
				<Link to={`/forms/${id}/responses`}>Responses</Link>
				<Link to={`/forms/${id}/statistics`}>Statistics</Link>
				<Link to={`/forms/${id}/sharing`}>Sharing</Link>
			</div> */}
			<Switch>
				<Route exact path={`/forms/${id}/responses`}>
					<FormResponses />
				</Route>
				<Route exact path={`/forms/${id}/statistics`}>
					<FormStatistics />
				</Route>
			</Switch>
		</>
	);
};

export default FormData;
