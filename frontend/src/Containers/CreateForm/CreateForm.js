import React, { useState } from "react";

import Button from "../../Components/Button";

import styles from "./CreateForm.module.css";

import { ReactComponent as Close } from "../../Assets/Images/close.svg";
import { ReactComponent as Add } from "../../Assets/Images/add.svg";

const CreateForm = () => {
	const [title, setTitle] = useState();
	const [fields, setFields] = useState([]);
	const [server, setServer] = useState();

	const addField = () => {
		setFields([...fields, { type: "text", title: "", options: [] }]);
	};

	const removeField = (index) => {
		setFields([...fields.slice(0, index), ...fields.slice(index + 1)]);
	};

	const changeField = (index, name, value) => {
		setFields([...fields.slice(0, index), { ...fields[index], [name]: value }, ...fields.slice(index + 1)]);
	};

	const changeOption = (fieldIndex, optionIndex, value) => {
		setFields([
			...fields.slice(0, fieldIndex),
			{
				...fields[fieldIndex],
				options: [
					...fields[fieldIndex].options.slice(0, optionIndex),
					value,
					...fields[fieldIndex].options.slice(optionIndex + 1),
				],
			},
			...fields.slice(fieldIndex + 1),
		]);
	};

	const handleSave = () => {
		console.log(fields);
	};

	const displayFields = fields.map((field, index) => (
		<div>
			<div className={styles.input_container}>
				<input
					type="text"
					placeholder="Enter Question"
					className={styles.text_field}
					value={field.title}
					name="title"
					onChange={({ target: { name, value } }) => changeField(index, name, value)}
				/>
				<select
					name="type"
					className={styles.select}
					onChange={({ target: { name, value } }) => changeField(index, name, value)}
				>
					<option>Text</option>
					<option>Multiple Choice</option>
				</select>
				<Close className={styles.close} onClick={() => removeField(index)} />
			</div>
			{field.type === "Multiple Choice" ? (
				<div className={styles.choices_container}>
					{field.options.map((option, optionIndex) => (
						<input
							type="text"
							className={styles.choice_input}
							placeholder="Enter Choice"
							value={option}
							onChange={({ target: { value } }) => changeOption(index, optionIndex, value)}
							autoFocus
						/>
					))}
				</div>
			) : null}
			{field.type === "Multiple Choice" ? (
				<div
					className={styles.add_container}
					onClick={() => changeField(index, "options", [...field.options, ""])}
				>
					<Add className={styles.add} />
					Add Choice
				</div>
			) : null}
			<hr className={styles.line} />
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
			<h3 className={styles.subtitle}>Select Server</h3>
			<select className={styles.select} value={server} onChange={({ target: { value } }) => setServer(value)}>
				<option>Server 1</option>
				<option>Server 2</option>
				<option>Server 3</option>
			</select>
			<Button title="Save" className={`${styles.save} ${styles.button}`} onClick={handleSave} />
		</div>
	);
};

export default CreateForm;
