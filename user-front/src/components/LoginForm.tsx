import {
  Box,
  FormControl,
  FormLabel,
  TextField
} from '@mui/material'
import { Dispatch, SetStateAction } from 'react'
import LoginType from '../types/Stations.Type';

interface Props {
  login: LoginType
  setLogin: Dispatch<SetStateAction<LoginType>>
}

const LoginForm = ({ login, setLogin }: Props) => (
  <FormControl>
    <FormLabel sx={{ paddingLeft: '18px' }} id='address-form'>Login</FormLabel>
    <Box
      component='form'
      sx={{
        display: 'flex',
        flexDirection: 'column',
        padding: '18px',
        height: '10em',
        justifyContent: 'space-between'
      }}
      autoComplete='off'
    >
      <TextField
        value={login.email}
        fullWidth
        id='email'
        label='Email'
        onChange={e => setLogin({ ...login, email: e.target.value })}
      />
      <TextField
        value={login.password}
        type="password"
        id='street-field'
        label='Senha'
        onChange={e => setLogin({ ...login, password: e.target.value })}
      />
    </Box>
  </FormControl>
)

export default LoginForm
