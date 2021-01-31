import React from 'react';
import Image from 'next/image';
import {Avatar, Tooltip} from '@material-ui/core';
import {makeStyles} from '@material-ui/core/styles';

export type ElectedOfficialAvatarProps = {
	id: string;
	political_party_id?: string;
	member_id?: string;
	is_active?: string;
	position?: string;
	state?: string;
};

const ElectedOfficialAvatar = (props: ElectedOfficialAvatarProps) => {
	const classes = useStyles();
	return (
		<Tooltip title="Sponsor">
			<Avatar className={classes.avatar}>
				<Image
					src={`/elected_official_images/congress/original/${props.member_id}.jpg`}
					alt={props.member_id}
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
	avatar: {
		// Border: 'thin solid red',
		width: theme.spacing(8),
		height: theme.spacing(8)
	}
}));

export default ElectedOfficialAvatar;
