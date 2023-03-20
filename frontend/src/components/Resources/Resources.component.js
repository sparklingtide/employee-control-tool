import { Space } from 'antd';
import { Telegram } from "./Telegram";
import { Gitlab } from "./Gitlab";
import { Discord } from "./Discord";
import { Monday } from "./Monday";
import { OpenVPN } from './OpenVPN';


export const Resources = () => {

  return (
    <Space
      direction="vertical"
      size="middle"
      style={{display: 'flex'}}
    >
      <OpenVPN/>
      <Telegram/>
      <Discord/>
      <Gitlab/>
      <Monday/>
    </Space>
  )
};
