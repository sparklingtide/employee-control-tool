import { Space } from 'antd';
import { Telegram } from "./Telegram";
import { Gitlab } from "./Gitlab";
import { Discord } from "./Discord";
import { Monday } from "./Monday";


export const Resources = () => {

  return (
    <Space
      direction="vertical"
      size="middle"
      style={{display: 'flex'}}
    >
      <Telegram/>
      <Discord/>
      <Gitlab/>
      <Monday/>
    </Space>
  )
};
