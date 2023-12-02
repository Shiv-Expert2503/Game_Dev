using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public UDPReceive udpReceive;
    public GameObject[] handpts;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = udpReceive.data;

        data = data.Remove(0,1);
        data = data.Remove(data.Length-1,1);
        print(data);

        string[] pts = data.Split(',');

        for (int i=0; i<21; i++)
        {
            // Float is used because in unity the object moves in very low changes of x,y,z so if int it will lead to 0 allthetime
            float x = 7 - float.Parse(pts[i*3]) / 90;   
            float y =  float.Parse(pts[i*3 +1]) / 90 - 2; 
            float z = float.Parse(pts[i*3 + 2]) / 90;
            handpts[i].transform.localPosition = new Vector3(x, y, z);
        }

    }
}
