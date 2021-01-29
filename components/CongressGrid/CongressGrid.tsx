import ElectedOfficialAvatar from "../ElectedOfficialAvatar/ElectedOfficialAvatar";
import { makeStyles } from "@material-ui/core/styles";
import React from "react";
import Grid from "@material-ui/core/Grid";
import type { ElectedOfficialAvatarProps } from "../ElectedOfficialAvatar/ElectedOfficialAvatar";

export type CongressGridProps = {
  electedOfficials: Array<ElectedOfficialAvatarProps>;
};

const CongressGrid = ({ electedOfficials }: CongressGridProps) => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <Grid container spacing={3} direction="row">
        {electedOfficials.map((electedOfficial) => (
          <Grid item xs key={electedOfficial.id}>
            <ElectedOfficialAvatar
              id={electedOfficial.id}
              political_party_id={electedOfficial.political_party_id}
              member_id={electedOfficial.member_id}
              is_active={electedOfficial.is_active}
              position={electedOfficial.position}
              state={electedOfficial.state}
            />
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

const useStyles = makeStyles(() => ({
  root: {
    flexGrow: 1,
  },
}));

export default CongressGrid;
