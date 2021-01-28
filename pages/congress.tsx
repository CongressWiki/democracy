import CongressGrid from "../components/CongressGrid";
import Layout from "../components/Layout";
import React from "react";
import { withApollo } from "../lib/with-apollo";

const Congress = () => {
  return (
    <Layout>
      <CongressGrid />
    </Layout>
  );
};

export default withApollo({ ssr: true })(Congress);
