import React from 'react';
import {
	Grid,
	Card,
	Typography,
	Avatar,
	Tooltip
	// Stepper,
	// Step,
	// StepLabel
} from '@material-ui/core';
import {makeStyles} from '@material-ui/core/styles';
import Skeleton from '@material-ui/lab/Skeleton';
import ElectedOfficialAvatar from '@components/ElectedOfficialAvatar/ElectedOfficialAvatar';

export type BillProps = {
	id: string;
	type: string;
	number: string;
	title: string;
	summary: string;
	actions: Array<Record<string, any>>;
	updated_at: Date;
	sponsor: string;
};

export const Bill = (props: BillProps) => {
	const classes = useStyles();
	const updated_at = new Date(props.updated_at).toDateString();

	return (
		<Card elevation={3} className={classes.root}>
			<Grid container spacing={1}>
				<Grid container justify="space-between">
					<Grid item xs={4}/>
					{/* ID */}
					<Grid item xs={4}>
						{props.id ? (
							<Typography variant="h6" align="center">
								{props.id}
							</Typography>
						) : (
							<Skeleton
								variant="text"
								animation="wave"
								height={22}
								width="30%"
							/>
						)}
					</Grid>
					{/* Date */}
					<Grid item xs={4}>
						{props.updated_at ? (
							<Typography display="block" align="right" variant="caption">
								{updated_at}
							</Typography>
						) : (
							<Skeleton
								variant="text"
								animation="wave"
								height={22}
								width="30%"
							/>
						)}
					</Grid>
				</Grid>

				{/* Title */}
				<Grid item xs={12}>
					{props.title ? (
						<Typography paragraph className={classes.title} variant="body1">
							{props.title}
						</Typography>
					) : (
						<Skeleton variant="text" animation="wave" height={22} width="80%"/>
					)}
				</Grid>

				{/* Stepper */}
				{/* <Stepper activeStep={props.actions.length - 1} alternativeLabel>
          {props.actions.map((action, index) => (
            <Step key={index}>
              <StepLabel>{action.text.slice(0, 60) + "..."}</StepLabel>
            </Step>
          ))}
        </Stepper> */}

				{/* Sponsor image */}
				<Grid item xs={4}/>
				<Grid item container xs={4} justify="center">
					<ElectedOfficialAvatar
						id={props.sponsor}
						preferred_name="Sponsor"
					/>
				</Grid>
				<Grid item xs={4}/>
			</Grid>
		</Card>
	);
};

const useStyles = makeStyles(theme => ({
	root: {
		flexGrow: 1,
		maxWidth: '600px',
		borderRadius: 5,
		padding: theme.spacing(2),
		border: 'thin solid',
		borderColor: theme.palette.secondary.main,
		boxShadow: '0 3px 5px 2px rgba(0, 0, 0, .1)',
		overflow: 'hidden'
	},
	sponsorAvatar: {
		width: theme.spacing(7),
		height: theme.spacing(7)
	},
	title: {
		paddingLeft: theme.spacing(3),
		paddingRight: theme.spacing(3)
	}
}));
