# API Reliability Monitor — SLA Report

> Last updated: **2026-07-15 22:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.46% | 2053.9 | 10206.7 | 1000ms | 267/1440 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.1 | 4595.4 | 1500ms | 4/1440 |
| ❌ | `ipapi_check` | 74.1% | 99.93% | 153.3 | 4507.0 | 2500ms | 1/1440 |
| ❌ | `nasa_apod` | 75.76% | 51.53% | 3214.9 | 11152.5 | 2000ms | 698/1440 |
| ❌ | `dog_ceo_random` | 94.93% | 96.6% | 543.2 | 10244.1 | 2500ms | 49/1440 |
| ⚠️ | `open_meteo_weather` | 98.68% | 97.15% | 720.6 | 14877.1 | 2000ms | 41/1440 |
| ⚠️ | `rest_countries` | 98.96% | 98.68% | 307.9 | 10221.5 | 2500ms | 19/1440 |
| ✅ | `useless_fact` | 99.65% | 99.72% | 634.3 | 10229.6 | 2500ms | 4/1440 |
| ✅ | `catfact_random` | 99.79% | 99.38% | 255.2 | 10080.2 | 3000ms | 9/1440 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.3 | 4328.4 | 1500ms | 1/1440 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.5 | 16112.2 | 2000ms | 4/1440 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 207.6 | 3882.8 | 2000ms | 2/1440 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4510.1 | 78.26% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 17:00 | 4003.6 | 54.05% |
| `nasa_apod` | 01:00 | 3752.8 | 54.55% |
| `numbers_trivia` | 03:00 | 3681.5 | 34.78% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 18:00 | 3561.3 | 50.65% |
| `nasa_apod` | 11:00 | 3500.9 | 51.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
