package test;

import java.util.ArrayList;
import java.util.Stack;

import workflow.util.instancehourdag.InstanceHourDag;

public class InstanceHourExample {

	private static ArrayList<Event> events;
	private static int eventNum;
	private static int chargeInterval;
	//0-45  75-115  123-188  250-285  290-330  335-370
	private static double[] pieces={0,45,75,115,123,188,250,285,290,330,335,370};
	public static void main(String[] args) {
		
		chargeInterval=60;
		
		events=new ArrayList<>();
		
		for(int i=0;i<pieces.length;i+=2)
			events.add(new Event(pieces[i], pieces[i+1]));
		
		eventNum=events.size();
		
		InstanceHourDag dag=new InstanceHourDag(eventNum-1+2);
		
		for(int i=0;i<eventNum;i++) {
			for(int j=i+1;j<eventNum+1;j++) {
				
				int instanceHour=(int) Math.ceil((events.get(j-1).finishTime-events.get(i).startTime)/chargeInterval);
				
				dag.addEage(i, j, instanceHour);
			}
		}
		
		dag.showDag();
		
		dag.findMinInstanceHour();
		
		dag.showArray();
		
		Stack<Integer> path=dag.getPathForMinIstsHour();
		
		double vmStartTime=events.get(path.pop()).startTime;
		double vmCloseTime;
		while(true) {
			vmCloseTime=events.get(path.peek()-1).finishTime;
			System.out.println("vm start time: "+vmStartTime+"  close time:"+vmCloseTime);
			if(path.size()==1)
				break;
			vmStartTime=events.get(path.pop()).startTime;
		}
	}
	
	
	
	
	
	public static class Event{
		private double startTime;
		private double finishTime;
		public Event(double startTime,double finishTime) {
			this.startTime=startTime;
			this.finishTime=finishTime;
		}
	}
}
