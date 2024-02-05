import HomeContainer from "../src/containers/HomeContainer";
import { Card, Box } from "@mui/material";

export default function AddBuildList() {
  return (
    <Card >
      <Box sx={{ border: "1px solid black", p: 0, m: 2 }}>
        <HomeContainer />
      </Box>
    </Card>
  )
}