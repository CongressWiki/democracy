import BillCanvas from "../components/BillCanvas";
import Layout from "../components/Layout";
import React from "react";
import { withApollo } from "../lib/with-apollo";

const Bills = () => {
  return (
    <Layout>
      <BillCanvas />
    </Layout>
  );
};

export default withApollo()(Bills);
