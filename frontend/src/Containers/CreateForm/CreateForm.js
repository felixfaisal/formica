import React, { useState } from "react";

import Button from "../../Components/Button";

import styles from "./CreateForm.module.css";

import { ReactComponent as Close } from "../../Assets/Images/close.svg";

const CreateForm = () => {
	const [title, setTitle] = useState();
	const [fields, setFields] = useState([]);

	const addField = () => {
		setFields([...fields, { type: "text", title: "" }]);
	};

	const changeQuestion = (index, question) => {
		setFields([...fields.slice(0, index), { ...fields[index], title: question }, ...fields.slice(index + 1)]);
	};

	const handleSave = () => {
		console.log(fields);
	};

	const displayFields = fields.map((field, index) => (
		<div className={styles.input_container}>
			<input
				type="text"
				placeholder="Enter Question"
				className={styles.text_field}
				value={field.title}
				onChange={({ target: { value } }) => changeQuestion(index, value)}
			/>
			<Close className={styles.close} />
		</div>
	));

	return (
		<div className={styles.container}>
			<input
				type="text"
				name="title"
				placeholder="Enter Title"
				className={styles.input}
				value={title}
				onChange={({ target: { value } }) => setTitle(value)}
			/>
			{displayFields}
			<Button title="Add Field" className={styles.button} onClick={addField} />

			<Button title="Save" className={`${styles.save} ${styles.button}`} onClick={handleSave} />
		</div>
	);
};

export default CreateForm;
