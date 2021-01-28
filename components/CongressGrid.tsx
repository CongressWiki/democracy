import { ElectedOfficialAvatar } from "./ElectedOfficialAvatar/ElectedOfficialAvatar";
import CircularProgress from "@material-ui/core/CircularProgress";
import { makeStyles } from "@material-ui/core/styles";
import React from "react";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import Grid from "@material-ui/core/Grid";

const GET_ELECTED_OFFICIALS = gql`
  query getElectedOfficials {
    elected_officials {
      id
      political_party_id
      member_id
      is_active
      position
      state
    }
  }
`;

const CongressGrid = () => {
  const { loading, error, data } = useQuery(GET_ELECTED_OFFICIALS);
  const classes = useStyles();

  if (loading) {
    return (
      <div className={classes.root}>
        <CircularProgress />
      </div>
    );
  }

  if (error) {
    return <span>Error {JSON.stringify(error, null, 2)}</span>;
  }

  if (data.elected_officials) {
    return (
      <div className={classes.root}>
        <Grid container spacing={3} direction="row">
          {data.elected_officials.map((elected_official) => (
            <Grid item xs key={elected_official.id}>
              <ElectedOfficialAvatar
                id={elected_official.id}
                political_party_id={elected_official.political_party_id}
                member_id={elected_official.member_id}
                is_active={elected_official.is_active}
                position={elected_official.position}
                state={elected_official.state}
              />
            </Grid>
          ))}
        </Grid>
      </div>
    );
  }
};

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
}));

export default CongressGrid;
