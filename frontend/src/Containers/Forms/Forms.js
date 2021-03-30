import React from "react";

import FormCard from "../../Components/FormCard";

import styles from "./Forms.module.css";

import forms from "../../Assets/Data/forms";

const Forms = () => {
	const displayForms = forms.map((form) => (
		<FormCard title={form.title} responses={form.responses} shared={form.shared} accepting={form.accepting} />
	));

	return <div className={styles.container}>{displayForms}</div>;
};

export default Forms;
