import React, { useEffect, useState } from "react";
import { Switch, Route, Link, useParams } from "react-router-dom";
import { useSelector } from "react-redux";

import FormResponses from "../FormResponses";
import FormStatistics from "../FormStatistics";
import Toast from "../../Components/Toast";

import { getFormResponsesService } from "../../Services/forms.service";

import styles from "./FormData.module.css";

const FormData = () => {
	const [loading, setLoading] = useState(true);
	const [formResponses, setFormResponses] = useState([]);
	const { id } = useParams();
	const { token } = useSelector((state) => state.auth);

	useEffect(() => {
		fetchFormResponses();
	}, []);

	const fetchFormResponses = async () => {
		try {
			const responses = await getFormResponsesService(token, id);
			const modifiedResponses = responses.map((response) => response.Response);
			setFormResponses(modifiedResponses);
			setLoading(false);
		} catch (err) {
			Toast("Some error has occurred", "error");
		}
	};

	return loading ? (
		<h3 className={styles.subtitle}>Please Wait...</h3>
	) : (
		<>
			<h3 className={styles.title}>Form {id} :- </h3>
			{/* <div className={styles.tabs}>
				<Link to={`/forms/${id}/responses`}>Responses</Link>
				<Link to={`/forms/${id}/statistics`}>Statistics</Link>
				<Link to={`/forms/${id}/sharing`}>Sharing</Link>
			</div> */}
			<Switch>
				<Route exact path={`/forms/${id}/responses`}>
					<FormResponses responses={formResponses} />
				</Route>
				<Route exact path={`/forms/${id}/statistics`}>
					<FormStatistics />
				</Route>
			</Switch>
		</>
	);
};

export default FormData;
