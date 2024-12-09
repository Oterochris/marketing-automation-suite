import React, { useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';

export function ContentCalendar() {
  const [events, setEvents] = useState([
    {
      id: 1,
      title: 'Product Launch Tweet',
      start: new Date(2024, 0, 15, 10, 0),
      end: new Date(2024, 0, 15, 11, 0),
      platform: 'twitter',
      status: 'scheduled'
    }
  ]);

  const handleEventDrop = ({ event, start, end }) => {
    const updatedEvents = events.map(e => 
      e.id === event.id ? { ...e, start, end } : e
    );
    setEvents(updatedEvents);
  };

  return (
    <div className="h-screen p-6">
      <div className="bg-white rounded-lg shadow-lg p-6 h-full">
        <h2 className="text-2xl font-bold mb-4">Content Calendar</h2>
        <Calendar
          localizer={momentLocalizer(moment)}
          events={events}
          startAccessor="start"
          endAccessor="end"
          onEventDrop={handleEventDrop}
          draggableAccessor={() => true}
          eventPropGetter={(event) => ({
            className: `bg-${event.platform}-500`
          })}
        />
      </div>
    </div>
  );
}