import { makeStyles } from "@material-ui/core/styles";

import React from "react";
import Skeleton from "@material-ui/lab/Skeleton";
import Avatar from "@material-ui/core/Avatar";
import Image from "next/image";
import { Tooltip } from "@material-ui/core";

export type ElectedOfficialAvatarProps = {
  id: string;
  political_party_id: string;
  member_id: string;
  is_active: string;
  position: string;
  state: string;
};

const ElectedOfficialAvatar = (props: ElectedOfficialAvatarProps) => {
  const classes = useStyles();

  return (
    <Tooltip title="Sponsor">
      <Avatar className={classes.avatar}>
        {
          <Image
            src={`/elected_official_images/congress/original/${props.member_id}.jpg`}
            alt={props.member_id}
            layout="fill"
            objectFit="cover"
            objectPosition="50% 5%"
            quality={75}
            onError={(e) => console.log(e)}
          />
        }
      </Avatar>
    </Tooltip>
  );
};

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    maxWidth: "600px",
    borderRadius: 5,
    padding: theme.spacing(2),
    border: "0.2em solid #edccab",
    boxShadow: "0 3px 5px 2px rgba(0, 0, 0, .1)",
    overflow: "hidden",
  },
  avatar: {
    width: theme.spacing(7),
    height: theme.spacing(7),
  },
  title: {
    paddingLeft: theme.spacing(3),
    paddingRight: theme.spacing(3),
  },
}));

export default ElectedOfficialAvatar;
