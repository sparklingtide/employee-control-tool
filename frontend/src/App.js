import React, { useState } from 'react';
import { Layout, Menu, theme } from 'antd';
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined
} from '@ant-design/icons';
import styles from './App.module.scss';
import { Groups } from './components/Groups';
import { Resources } from './components/Resources';
import { Employees } from './components/Employees';
import { SignIn } from './components/SignIn';
import useToken from './components/useToken';

const { Header, Sider, Content } = Layout;

function getItem(label, key, content) {
  return {
    label,
    key,
    content
  }
}

const App = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [content, setContent] = useState();
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const { accessToken, setToken } = useToken();

  if (!accessToken) {
    return <SignIn setToken={setToken} />
  }

  const items = [
    getItem("groups", "groups", Groups),
    getItem("resources", "resources", Resources),
    getItem("employees", "employees", Employees)
  ];

  const changeContent = (props) => {
    let content = items.find(obj => {
      return obj.label === props.key
    });
    setContent(content.content);
  }


  return (
    <Layout className={styles.appContainer}>
      <Sider trigger={null} collapsible collapsed={collapsed}>
        <div className={styles.logo} />
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={['groups']}
          items={items}
          onSelect={changeContent}
        />
      </Sider>
      <Layout className="site-layout">
        <Header style={{ padding: 0, background: colorBgContainer }}>
          {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
            className: styles.trigger,
            onClick: () => setCollapsed(!collapsed),
          })}
        </Header>
        <Content
          style={{
            margin: '24px 16px',
            padding: 24,
            background: colorBgContainer,
            overflow: "initial"
          }}
        >
          {content}
        </Content>
      </Layout>
    </Layout>
  );
};

export default App;
