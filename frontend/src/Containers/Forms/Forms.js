import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import FormCard from "../../Components/FormCard";
import Toast from "../../Components/Toast";

import { getForms } from "../../Redux/ActionCreators/forms.creator";

import styles from "./Forms.module.css";

const Forms = () => {
	const [loading, setLoading] = useState(true);

	const { forms } = useSelector((state) => state.forms);
	const dispatch = useDispatch();

	useEffect(() => {
		fetchForms();
	}, []);

	const fetchForms = async () => {
		try {
			await dispatch(getForms());
		} catch (err) {
			Toast("An error has occurred, please try again!", "error");
		} finally {
			setLoading(false);
		}
	};

	const displayForms = forms.map((form) => (
		<FormCard
			title={form.FormName}
			id={form.FormName}
			responses={[]}
			// shared={form.shared}
			// accepting={form.accepting}
		/>
	));

	return loading ? (
		<div className={styles.container}>
			<h3 className={styles.subtitle}>Please Wait...</h3>
		</div>
	) : (
		<div className={styles.container}>{displayForms}</div>
	);
};

export default Forms;
