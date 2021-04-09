import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import Button from "../../Components/Button";
import Toast from "../../Components/Toast";

import { getUserServers } from "../../Redux/ActionCreators/user.creator";
import { createForm } from "../../Redux/ActionCreators/forms.creator";

import { getServerChannelsService } from "../../Services/users.service";

import styles from "./CreateForm.module.css";

import { ReactComponent as Close } from "../../Assets/Images/close.svg";
import { ReactComponent as Add } from "../../Assets/Images/add.svg";

const CreateForm = () => {
	const { token } = useSelector((state) => state.auth);
	const { userId, servers } = useSelector((state) => state.user);
	const dispatch = useDispatch();

	const [loading, setLoading] = useState(true);
	const [title, setTitle] = useState();
	const [fields, setFields] = useState([]);
	const [server, setServer] = useState();
	const [channels, setChannels] = useState([]);
	const [channel, setChannel] = useState();
	const [loadingChannels, setLoadingChannels] = useState(false);

	const addField = () => {
		setFields([...fields, { input_type: "text", question: "", options: [], question_id: 0 }]);
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

	useEffect(() => {
		getServers();
	}, []);

	// useEffect(() => {
	// 	getChannels();
	// }, [server]);

	const getServers = async () => {
		try {
			await dispatch(getUserServers());
			setLoading(false);
		} catch (err) {
			console.log(err);
		}
	};

	const getChannels = async () => {
		try {
			setLoadingChannels(true);
			console.log(servers);
			const serverId = server ? server.split(" ").pop().match(/\d+/g)[0] : servers[0].id;

			console.log(token, serverId);
			const channels = await getServerChannelsService(token, serverId);
			console.log(channels);
			if (Array.isArray(channels)) setChannels(channels);
			else setChannels([]);

			setLoadingChannels(false);
		} catch (err) {
			console.log(err);
			Toast("Some error has occurred!", "error");
		}
	};

	const handleSave = async () => {
		try {
			// if (channels.length === 0) {
			// 	Toast("Please add bot to server!", "error");
			// 	return;
			// }
			setLoading(true);
			const modifiedFields = fields.map((field) => ({ ...field, input_type: field.input_type.toLowerCase() }));
			const formData = {
				userid: userId,
				FormName: title,
				Formfields: modifiedFields,
				serverid: server ? server.split(" ").pop().match(/\d+/g)[0] : servers[0].id,
				// channelid: channel ? server.split(" ").pop().match(/\d+/g)[0] : channels[0].id,
			};

			await dispatch(createForm(formData));

			Toast("Form Created Successfully!", "success");

			setTitle("");
			setFields([]);
			setServer(null);
		} catch (err) {
			console.log(err);
			Toast("Some error has occured, please try again!", "error");
		} finally {
			setLoading(false);
		}
	};

	const displayFields = fields.map((field, index) => (
		<div>
			<div className={styles.input_container}>
				<input
					type="text"
					placeholder="Enter Question"
					className={styles.text_field}
					value={field.question}
					name="question"
					onChange={({ target: { name, value } }) => changeField(index, name, value)}
					autoFocus
				/>
				<select
					name="input_type"
					className={styles.select}
					onChange={({ target: { name, value } }) => changeField(index, name, value)}
				>
					<option>Text</option>
					<option>Number</option>
					<option>Multiple Choice</option>
					<option>Email</option>
					<option>Phone</option>
				</select>
				<Close className={styles.close} onClick={() => removeField(index)} />
			</div>
			{field.input_type === "Multiple Choice" ? (
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
			{field.input_type === "Multiple Choice" ? (
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

	return loading ? (
		<div className={styles.container}>
			<h3 className={styles.subtitle}>Please Wait...</h3>
		</div>
	) : (
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
				{servers.map((server) => (
					<option>
						{server.name} ({server.id})
					</option>
				))}
			</select>
			{/* <h3 className={styles.subtitle}>Select Channel</h3>
			<select className={styles.select} value={channel} onChange={({ target: { value } }) => setChannel(value)}>
				{loadingChannels ? (
					<option>Please Wait...</option>
				) : (
					channels.map((channel) => (
						<option>
							{channel.name} ({channel.id})
						</option>
					))
				)}
			</select> */}
			<Button title="Save" className={`${styles.save} ${styles.button}`} onClick={handleSave} />
		</div>
	);
};

export default CreateForm;
