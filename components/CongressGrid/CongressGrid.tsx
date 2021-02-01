import React from 'react';
import {Grid} from '@material-ui/core';
import ElectedOfficialAvatar from '../ElectedOfficialAvatar/ElectedOfficialAvatar';
import type {ElectedOfficialAvatarProps} from '../ElectedOfficialAvatar/ElectedOfficialAvatar';

export type CongressGridProps = {
	electedOfficials: ElectedOfficialAvatarProps[];
};

const CongressGrid = ({electedOfficials}: CongressGridProps) => {
	return (
		<Grid container spacing={3} direction="row">
			{electedOfficials.map(electedOfficial => (
				<Grid key={electedOfficial.id} item xs>
					<ElectedOfficialAvatar
						id={electedOfficial.id}
						preferred_name={electedOfficial.preferred_name}
						political_party={electedOfficial.political_party}
						type={electedOfficial.type}
						state={electedOfficial.state}
					/>
				</Grid>
			))}
		</Grid>
	);
};

export default CongressGrid;
