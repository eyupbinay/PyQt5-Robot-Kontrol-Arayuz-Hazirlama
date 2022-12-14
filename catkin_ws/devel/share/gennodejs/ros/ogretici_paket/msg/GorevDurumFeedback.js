// Auto-generated. Do not edit!

// (in-package ogretici_paket.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class GorevDurumFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.oran = null;
    }
    else {
      if (initObj.hasOwnProperty('oran')) {
        this.oran = initObj.oran
      }
      else {
        this.oran = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GorevDurumFeedback
    // Serialize message field [oran]
    bufferOffset = _serializer.string(obj.oran, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GorevDurumFeedback
    let len;
    let data = new GorevDurumFeedback(null);
    // Deserialize message field [oran]
    data.oran = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.oran);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ogretici_paket/GorevDurumFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'abfa1fb1b715e7ce91c4950a3d2cbd0b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    string oran
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GorevDurumFeedback(null);
    if (msg.oran !== undefined) {
      resolved.oran = msg.oran;
    }
    else {
      resolved.oran = ''
    }

    return resolved;
    }
};

module.exports = GorevDurumFeedback;
