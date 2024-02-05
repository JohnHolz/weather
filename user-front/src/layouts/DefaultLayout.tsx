import ResponsiveAppBar from "../components/ResponsiveAppBar";
import { Box } from "@mui/material";
import Footer from "../components/Footer";
import Head from "next/head";

interface Props {
  children: React.ReactNode;
}

const DefaultLayout = ({ children }: Props) => (
  <Box
    sx={{
      marginTop: "75px",
      padding: "20px",
      display: "center",
      backgroundColor: "#747d8c",
    }}
  >
    <Head>
      <title>Net</title>
      <meta name="description" content="Haus" />
      <link rel="icon" href="/white-cloud.png" />
    </Head>
    <ResponsiveAppBar />
    {children}
    {/* <Footer /> */}
  </Box>
);

export default DefaultLayout;
