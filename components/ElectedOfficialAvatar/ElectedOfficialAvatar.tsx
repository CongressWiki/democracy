import React from 'react';
import Image from 'next/image';
import {Avatar, Tooltip} from '@material-ui/core';
import {makeStyles} from '@material-ui/core/styles';

export type ElectedOfficialAvatarProps = {
	id: string;
	preferred_name?: string;
	political_party?: string;
	type?: string;
	state?: string;
};

const ElectedOfficialAvatar = (props: ElectedOfficialAvatarProps) => {
	const classes = useStyles();
	const partyThemedBorderClass = party => {
		if (party === 'Republican') {
			return classes.republicanBorder;
		}

		if (party === 'Democrat') {
			return classes.democraticBorder;
		}

		if (party === 'Independent') {
			return classes.independentBorder;
		}

		console.warn('Unhandled political party');
		return classes.otherBorder;
	};

	return (
		<Tooltip title={props.preferred_name}>
			<Avatar className={`${classes.avatar} ${partyThemedBorderClass(props.political_party)}`}>
				<Image
					src={`/elected_official_images/congress/original/${props.id}.jpg`}
					alt={props.preferred_name}
					layout="fill"
					objectFit="cover"
					objectPosition="50% 5%"
					quality={75}
				/>
			</Avatar>
		</Tooltip>
	);
};

const useStyles = makeStyles(theme => ({
	otherBorder: {
		border: 'thin solid grey'
	},
	independentBorder: {
		border: 'thin solid green'
	},
	republicanBorder: {
		border: 'thin solid red'
	},
	democraticBorder: {
		border: 'thin solid blue'
	},
	avatar: {
		width: theme.spacing(8),
		height: theme.spacing(8)
	}
}));

export default ElectedOfficialAvatar;
