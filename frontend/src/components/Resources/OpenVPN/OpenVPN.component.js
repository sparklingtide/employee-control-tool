import { useState, useEffect } from "react";
import { Space, Switch, Table, Typography} from 'antd';
import { axiosInstance } from "../../../models/axiosInstance";



export const OpenVPN = () => {
  const columns = [
    {
      title: "Host",
      dataIndex: "openvpn_host",
      key: "host"
    },
    {
      title: "Port",
      dataIndex: "openvpn_port",
      key: "port"
    },
    {
      title: "Vault URL",
      dataIndex: "vault_url",
      key: "vault_url"
    },
    {
      title: "Actions",
      dataIndex: "",
      width: "20%",
      render: (_, record) => (
        <span>
          <Typography.Link
            style={{
              marginRight: 8
            }}
          >
            Edit
          </Typography.Link>

          <Typography.Link>
            Delete
          </Typography.Link>
        </span>
      )
    }
  ]


  const [data, setData] = useState([]);
  useEffect(() => {
    axiosInstance.get("/providers/openvpn/").then(res => setData(res.data));
  }, []);

  return (
    <Table
      columns={columns}
      dataSource={data}
      title={() => "OpenVPN resources"}
    />
  )
};
