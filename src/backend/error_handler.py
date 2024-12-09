from typing import Dict

def handle_error(error: Dict) -> Dict:
    error_responses = {
        'database': {
            'status': 'error',
            'message': 'Database error occurred. Please try again later.',
            'code': 'DB_ERROR'
        },
        'authentication': {
            'status': 'error',
            'message': 'Authentication failed. Please check your credentials.',
            'code': 'AUTH_ERROR'
        },
        'rate_limit': {
            'status': 'error',
            'message': 'Rate limit exceeded. Please try again later.',
            'code': 'RATE_LIMIT'
        },
        'input': {
            'status': 'error',
            'message': 'Invalid input provided.',
            'code': 'INPUT_ERROR'
        }
    }
    
    return error_responses.get(error['type'], {
        'status': 'error',
        'message': 'An unknown error occurred.',
        'code': 'UNKNOWN'
    })