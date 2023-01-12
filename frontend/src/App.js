import React, { useState } from 'react';
import { Layout, Menu, theme, Space } from 'antd';
import styles from './App.module.scss';
import { Groups } from './components/Groups';
import { Resources } from './components/Resources';
import { Employees } from './components/Employees';
import { SignIn } from './components/SignIn';
import useToken from './components/useToken';

const { Header, Content } = Layout;

function getItem(label, key, content) {
  return {
    label,
    key,
    content
  }
}

const App = () => {
  const [content, setContent] = useState();
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const { accessToken, setToken } = useToken();

  if (!accessToken) {
    return (
      <Layout className={styles.appContainer}>
        <Space>
          <SignIn setToken={setToken} />
        </Space>
      </Layout>
    )
  }

  const items = [
    getItem("groups", "groups", <Groups/>),
    getItem("resources", "resources", <Resources/>),
    getItem("employees", "employees", <Employees/>)
  ];

  const changeContent = (props) => {
    let content = items.find(obj => {
      return obj.label === props.key
    });
    setContent(content.content);
  }


  return (
    <Layout className={styles.appContainer}>
      <Header
        style={{
          position: 'sticky',
          top: 0,
          zIndex: 1,
          width: '100%',
        }}
      >
        <div
          style={{
            float: 'left',
            width: 120,
            height: 31,
            margin: '16px 24px 16px 0',
            background: 'rgba(255, 255, 255, 0.2)',
          }}
        />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['groups']}
          items={items}
          onSelect={changeContent}
        />
      </Header>

      <Content
        className="site-layout"
        style={{
          margin: '24px 16px',
          padding: 24,
          background: colorBgContainer,
          overflow: "auto"
        }}
      >
        {content}
      </Content>

    </Layout>
  );
};

export default App;
