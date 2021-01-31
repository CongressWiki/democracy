import React from 'react';
import {
	CircularProgress as MaterialUiProgress
} from '@material-ui/core';
import {makeStyles} from '@material-ui/core/styles';

const CircularProgress = () => {
	const styles = useStyles();
	return (
		<div className={styles.container}>
			<MaterialUiProgress color="secondary"/>
		</div>
	);
};

const useStyles = makeStyles(() => ({
	container: {
		display: 'flex',
		height: '90vh',
		justifyContent: 'center',
		alignItems: 'center'
	}
}));

export default CircularProgress;
