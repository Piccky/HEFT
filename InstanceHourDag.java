package workflow.util.instancehourdag;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Stack;


public class InstanceHourDag {

	private int size;
	private int[] minHours;  //从开始节点到每个节点最短的距离
	private int[] precursors;  //节点在其与开始节点最短路线中的前驱节点
	private LinkedHashMap<Integer, LinkedHashMap<Integer,Integer >> eages;
	
	public InstanceHourDag(int size) {
		
		this.size=size;
		eages=new LinkedHashMap<>();
		for(int i=0;i<size-1;i++) {
			eages.put(i, new LinkedHashMap<Integer,Integer>());
		}
		minHours=new int[size];    //从开始节点到每个节点最短的距离
		precursors=new int[size];  //节点在其与开始节点最短路线中的前驱节点
		minHours[0]=0;  //开始节点到本身是0
		precursors[0]=0;  //开始节点在其与开始节点最短路线中的前驱节点是它本身
		for(int i=1;i<size;i++) {
			minHours[i]=Integer.MAX_VALUE;
			precursors[i]=-1;
		}
	}
	public void findMinInstanceHour() {
		for(int i=1;i<size;i++) {
			//开始节点到第i个节点的最短路径
			minHours[i]=eages.get(0).get(i);
			precursors[i]=0;
			for(int j=i-1;j>0;j--) {
				if(minHours[j]+eages.get(j).get(i)<minHours[i]) {
					minHours[i]=minHours[j]+eages.get(j).get(i);
					precursors[i]=j;
				}
			}
		}
	}
	public void addEage(int sourceId,int destId,int value) {
		eages.get(sourceId).put(destId, value);
	}
	public void showDag() {
		for(int sourceId:eages.keySet()) {
			System.out.println("node_"+sourceId+"’s eages:");
			for(int destId:eages.get(sourceId).keySet()) {
				System.out.println("   child id:"+destId+"  value:"+eages.get(sourceId).get(destId));
			}
		}
	}
	
	public int getMinInstanceHour() {
		findMinInstanceHour();
		return minHours[size-1];
	}
	public void showArray() {
		System.out.println("minHours:");
		for(int i=0;i<size;i++) {
			System.out.print(minHours[i]+" ");
		}
		System.out.println();
		System.out.println("precursors:");
		for(int i=0;i<size;i++) {
			System.out.print(precursors[i]+" ");
		}
		System.out.println();
	}
	/**
	 * 获取使实例小时最少的路径
	 * 出栈时，类似于0,1,3,6（size-1）
	 * 
	 */
	public Stack<Integer> getPathForMinIstsHour() {
		Stack<Integer> MinPath=new Stack<>();
		int id=size-1;
		MinPath.push(id);
		while(id!=0) {
			MinPath.push(precursors[id]);
			id=precursors[id];
		}
		return MinPath;
	}
}
