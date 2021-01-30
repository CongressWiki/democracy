import React from 'react';
import {
	CircularProgress as MaterialUiProgress,
	Backdrop
} from '@material-ui/core';
import {makeStyles} from '@material-ui/core/styles';

const CircularProgress = () => {
	const styles = useStyles();
	return (
		<div className={styles.container}>
			<Backdrop open transitionDuration={5000}>
				<MaterialUiProgress color="secondary"/>
			</Backdrop>
		</div>
	);
};

const useStyles = makeStyles(() => ({
	container: {
		display: 'flex',
		height: '70vh',
		justifyContent: 'center',
		alignItems: 'center',
		textAlign: 'center'
	}
}));

export default CircularProgress;
